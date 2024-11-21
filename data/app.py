from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def query_db(query):
    conn = sqlite3.connect('data.db')
    result = conn.execute(query).fetchall()
    conn.commit()
    conn.close()
    return result

def json_to_row(d):
    grid = d['grid']
    game_id = 0
    flat_grid = {
        'r0c0': grid[0][0], 'r1c0': grid[0][1], 'r2c0': grid[0][2], 'r3c0': grid[0][3],
        'r0c1': grid[1][0], 'r1c1': grid[1][1], 'r2c1': grid[1][2], 'r3c1': grid[1][3],
        'r0c2': grid[2][0], 'r1c2': grid[2][1], 'r2c2': grid[2][2], 'r3c2': grid[2][3],
        'r0c3': grid[3][0], 'r1c3': grid[3][1], 'r2c3': grid[3][2], 'r3c3': grid[3][3]
    }

    vals = [d['game_id'], '"' + d['move'] + '"', d['timestamp'], d['score'],
        flat_grid['r0c0'], flat_grid['r1c0'], flat_grid['r2c0'], flat_grid['r3c0'],
        flat_grid['r0c1'], flat_grid['r1c1'], flat_grid['r2c1'], flat_grid['r3c1'],
        flat_grid['r0c2'], flat_grid['r1c2'], flat_grid['r2c2'], flat_grid['r3c2'],
        flat_grid['r0c3'], flat_grid['r1c3'], flat_grid['r2c3'], flat_grid['r3c3']
    ]

    return '(' + (','.join(map(str,vals))) + ')'


@app.route('/add', methods=['POST'])
def insert_to_db():
    data = request.get_json()

    rows = list(map(json_to_row, data['data']))

    query = f"""INSERT INTO MOVES (game, move, timestamp, score, r0c0, r1c0, r2c0, r3c0, r0c1, r1c1, r2c1, r3c1, r0c2, r1c2, r2c2, r3c2, r0c3, r1c3, r2c3, r3c3) VALUES
    """

    query += ',\n'.join(rows)

    print(query)

    print(query_db(query))

    return jsonify({'message': 'row added'})

if __name__ == '__main__':
    app.run(debug=True)

