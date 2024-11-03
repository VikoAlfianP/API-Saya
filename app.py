from flask import Flask, jsonify, request

app = Flask(__name__)

# Contoh data awal (database dummy)
laptops = [
    {"id": 1, "brand": "Dell", "model": "XPS 13", "price": 15000000, "stock": 10},
    {"id": 2, "brand": "Apple", "model": "MacBook Pro", "price": 25000000, "stock": 5},
    {"id": 3, "brand": "Asus", "model": "ZenBook", "price": 12000000, "stock": 8}
]

# Endpoint untuk mendapatkan daftar laptop
@app.route('/laptops', methods=['GET'])
def get_laptops():
    return jsonify(laptops)

# Endpoint untuk mendapatkan detail laptop berdasarkan ID
@app.route('/laptops/<int:laptop_id>', methods=['GET'])
def get_laptop(laptop_id):
    laptop = next((l for l in laptops if l["id"] == laptop_id), None)
    if laptop:
        return jsonify(laptop)
    return jsonify({"message": "Laptop not found"}), 404

# Endpoint untuk menambahkan laptop baru
@app.route('/laptops', methods=['POST'])
def add_laptop():
    new_laptop = request.get_json()
    new_laptop["id"] = laptops[-1]["id"] + 1 if laptops else 1
    laptops.append(new_laptop)
    return jsonify(new_laptop), 201

# Endpoint untuk memperbarui data laptop berdasarkan ID
@app.route('/laptops/<int:laptop_id>', methods=['PUT'])
def update_laptop(laptop_id):
    laptop = next((l for l in laptops if l["id"] == laptop_id), None)
    if laptop:
        data = request.get_json()
        laptop.update(data)
        return jsonify(laptop)
    return jsonify({"message": "Laptop not found"}), 404

# Endpoint untuk menghapus laptop berdasarkan ID
@app.route('/laptops/<int:laptop_id>', methods=['DELETE'])
def delete_laptop(laptop_id):
    global laptops
    laptops = [l for l in laptops if l["id"] != laptop_id]
    return jsonify({"message": "Laptop deleted"})

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
