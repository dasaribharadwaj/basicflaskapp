from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/sort_numbers', methods=['POST'])
def sort_numbers():
    # Get the list of numbers from the request body
    numbers = request.json['numbers']

    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    return jsonify(sorted_numbers)


if __name__ == '__main__':
   app.run()


# srinivas@alvyl.com
