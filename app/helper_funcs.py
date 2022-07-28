from flask import Blueprint, request, jsonify, make_response, abort
from app.models.inventory import Inventory

def inv_validation(inv_id):
    try: 
        inv_id = int(inv_id)
    except ValueError: 
        abort(make_response({'msg': f"The inventory id {inv_id} is invalid. The id must be an integer."}, 400))

    inventories = Inventory.query.all()
    for inventory in inventories: 
        if inventory.id == inv_id:
            return inventory
    abort(make_response({'msg': f"The inventory id {inv_id} was not found."}, 404))

# def request_body_validation(request_body):
#     if "inv_date" not in request_body \
#         or "family" not in request_body \
#         or "facility" not in request_body \
#         or "tank" not in request_body \
#         or "task_id" not in request_body \
#         or "total_animals" not in request_body \
#         or "shell_lengths" not in request_body: 
#         return jsonify({'msg': 'Invalid Data: Request missing required field'}), 400