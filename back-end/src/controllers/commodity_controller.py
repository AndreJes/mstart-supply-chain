from flask import Blueprint, jsonify, request, Response
from services import CommodityService as service_class
from models import Commodity as model

bp = Blueprint('commodity', __name__, url_prefix="/commodities")

service = service_class()

@bp.route("/", methods=["GET"])
def list_all():
    results = service.list_all()
    return jsonify(results)

@bp.route("/", methods=["POST"])
def add():
    body = request.get_json()
    results = service.insert(model.from_dict(body))
    return jsonify(results)

@bp.route("/<id>", methods=["GET"])
def get(id):
    results = service.get(id)
    return jsonify(results)

@bp.route("/<id>", methods=["PATCH"])
def update(id):
    body = request.get_json()
    results = service.update(id, body)
    return jsonify(results)

@bp.route("/<id>", methods=["DELETE"])
def delete(id):
    results = service.delete(id)
    return Response(None, status=204)