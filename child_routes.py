from flask import Blueprint, jsonify, request

child_bp = Blueprint('child', __name__)

# --- Goals Management ---
@child_bp.route('/goals', methods=['GET'])
def get_goals():
    return jsonify({'message': 'Get all goals'})

@child_bp.route('/goals', methods=['POST'])
def create_goal():
    return jsonify({'message': 'Create new goal'})

@child_bp.route('/goals/<int:goal_id>', methods=['GET'])
def get_goal(goal_id):
    return jsonify({'message': f'Get goal {goal_id}'})

@child_bp.route('/goals/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    return jsonify({'message': f'Update goal {goal_id}'})

@child_bp.route('/goals/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    return jsonify({'message': f'Delete goal {goal_id}'})

@child_bp.route('/goals/<int:goal_id>/progress', methods=['PATCH'])
def patch_goal_progress(goal_id):
    return jsonify({'message': f'Update progress for goal {goal_id}'})

# --- Spending ---
@child_bp.route('/spends', methods=['GET'])
def get_spends():
    return jsonify({'message': 'Get all spends'})

@child_bp.route('/spends', methods=['POST'])
def create_spend():
    return jsonify({'message': 'Create spend'})

@child_bp.route('/spends/<int:spend_id>', methods=['GET'])
def get_spend(spend_id):
    return jsonify({'message': f'Get spend {spend_id}'})

@child_bp.route('/spends/<int:spend_id>', methods=['PUT'])
def update_spend(spend_id):
    return jsonify({'message': f'Update spend {spend_id}'})

@child_bp.route('/spends/<int:spend_id>', methods=['DELETE'])
def delete_spend(spend_id):
    return jsonify({'message': f'Delete spend {spend_id}'})

@child_bp.route('/spends/categories', methods=['GET'])
def get_spend_categories():
    return jsonify({'message': 'Get spend categories'})

# --- Pocket Money ---
@child_bp.route('/money-sources', methods=['GET'])
def get_money_sources():
    return jsonify({'message': 'Get money sources'})

@child_bp.route('/money-sources', methods=['POST'])
def create_money_source():
    return jsonify({'message': 'Create money source'})

@child_bp.route('/money-sources/<int:source_id>', methods=['PUT'])
def update_money_source(source_id):
    return jsonify({'message': f'Update money source {source_id}'})

@child_bp.route('/money-sources/<int:source_id>', methods=['DELETE'])
def delete_money_source(source_id):
    return jsonify({'message': f'Delete money source {source_id}'})

@child_bp.route('/balance', methods=['GET'])
def get_balance():
    return jsonify({'message': 'Get child balance'})

# --- Challenges ---
@child_bp.route('/challenges/current', methods=['GET'])
def get_current_challenges():
    return jsonify({'message': 'Get current challenges'})

@child_bp.route('/challenges/history', methods=['GET'])
def get_challenge_history():
    return jsonify({'message': 'Get challenge history'})

@child_bp.route('/challenges/<int:challenge_id>/complete', methods=['POST'])
def complete_challenge(challenge_id):
    return jsonify({'message': f'Complete challenge {challenge_id}'})

# --- Tips ---
@child_bp.route('/tips/weekly', methods=['GET'])
def get_weekly_tips():
    return jsonify({'message': 'Get weekly tips'})

@child_bp.route('/tips/archive', methods=['GET'])
def get_tip_archive():
    return jsonify({'message': 'Get tip archive'})