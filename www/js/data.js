var data_array = []
const server_URI = "http://localhost:5000/add"
const batch_size = 10
var game_id = ""

function add_move_data(m) {
    console.log("Move ${m} detected")

    var grid = gm.grid.cells.map(col => col.map(tile => tile == null ? 0 : tile.value))
    var m_text = ['U','R','D','L'][m]

    data_array.push({
        'game_id': game_id,
        'grid': grid,
        'score': gm.score,
        'move': m_text,
        'timestamp': Date.now()
    })

    if (data_array.length >= batch_size) {
        temp_array = data_array
        data_array = []
        send_data_to_sql(temp_array);
    }
}

function send_data_to_sql(data_array) {
    fetch(server_URI, {
        method: "POST",
        body: JSON.stringify({
            data: data_array
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            "Access-Control-Allow-Origin": "*"
        }
    })

}
