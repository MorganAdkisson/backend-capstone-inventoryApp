from flask import Blueprint, request, jsonify, make_response, abort
from app.models.inventory import Inventory
from app import db
from app.helper_funcs import *

hello_world_bp = Blueprint("hello_world", __name__)
@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    response = "Hello, World!"
    return response

inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")
@inventory_bp.route("", methods=["POST"])
def create_inventory():
    request_body = request.get_json()

    # opportunity for a helper function?
    if "inv_date" not in request_body \
        or "family" not in request_body \
        or "facility" not in request_body \
        or "tank" not in request_body \
        or "task_id" not in request_body \
        or "total_animals" not in request_body \
        or "shell_lengths" not in request_body: 
        return jsonify({'msg': 'Invalid Data: Request missing required field.'}), 400

    new_inventory = Inventory(
        inv_date = request_body["inv_date"], 
        family = request_body["family"], 
        facility = request_body["facility"], 
        tank = request_body["tank"], 
        task_id = request_body["task_id"], 
        total_animals = request_body["total_animals"], 
        shell_lengths = request_body["shell_lengths"], 
    )

    db.session.add(new_inventory)
    db.session.commit()
    return jsonify(new_inventory.to_dict()), 201

@inventory_bp.route("", methods=["GET"])
def get_all_inventory():
    inventories = Inventory.query.all()
    return jsonify([inventory.to_dict() for inventory in inventories]), 200

@inventory_bp.route("/<inv_id>", methods=["GET"])
def get_one_inventory(inv_id):
    inventory = inv_validation(inv_id)
    return jsonify(inventory.to_dict()), 200

@inventory_bp.route("/<inv_id>", methods=["DELETE"])
def delete_inventory(inv_id):
    inventory = inv_validation(inv_id)
    db.session.delete(inventory)
    db.session.commit()
    return jsonify(f"Inventory with id {inv_id} successfully deleted"), 200 

@inventory_bp.route("/<inv_id>", methods=["PUT"])
def update_inventory(inv_id):
    inventory = inv_validation(inv_id)
    request_body = request.get_json()
    # # TODO Can this be cleaned up a bit more? 
    # # Also does not work if only one updated key:value pair is input. As it's written now all attributes must be included in request. 
    # for item in request_body: 
    #     inventory.item = request_body[item]
    inventory.inv_date = request_body["inv_date"]
    inventory.family = request_body["family"]
    inventory.facility = request_body["facility"]
    inventory.tank = request_body["tank"]
    inventory.task_id = request_body["task_id"]
    inventory.total_animals = request_body["total_animals"]
    inventory.shell_lengths = request_body["shell_lengths"]
    db.session.commit()
    return jsonify(inventory.to_dict()), 200
