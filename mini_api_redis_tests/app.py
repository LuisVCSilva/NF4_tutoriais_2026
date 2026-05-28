from flask import Flask, request, jsonify

from calculator import add

from database import db
from cache import get_cache, set_cache

import random
import time
import datetime

app = Flask(__name__)


@app.route("/sum", methods=["POST"])
def sum_route():

    data = request.json

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:

        return jsonify({
            "error": "Missing parameters"
        }), 400

    result = add(a, b)
    print(result)
    return jsonify({
        "result": result
    })


@app.route("/pi", methods=["POST"])
def compute_pi():

    data = request.json or {}

    samples = data.get(
        "samples",
        1_000_000
    )

    cache_key = f"pi:{samples}"

    cached = get_cache(cache_key)

    if cached:

        cached["cached"] = True

        return jsonify(cached)

    start = time.time()

    inside = 0

    for _ in range(samples):

        x = random.random()
        y = random.random()

        if x*x + y*y <= 1:
            inside += 1

    pi = 4 * inside / samples

    elapsed = time.time() - start

    result = {
        "cached": False,
        "samples": samples,
        "pi": pi,
        "elapsed_seconds": elapsed
    }

    # salva no redis
    set_cache(
        cache_key,
        result,
        ttl=3600
    )

    # salva no tinydb
    db.insert({
        "timestamp": str(datetime.datetime.now()),
        "samples": samples,
        "pi": pi,
        "elapsed_seconds": elapsed
    })
    print(result)
    return jsonify(result)


@app.route("/history", methods=["GET"])
def history():

    data = db.all()
    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

