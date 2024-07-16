from flask import Blueprint, request, jsonify
from app.models import QnA, db
from app.openai_client import get_answer
bp = Blueprint('routes', __name__)

@bp.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({'error': 'Question is required'}), 400

    answer = get_answer(question)
    qna = QnA(question=question, answer=answer)
    db.session.add(qna)
    db.session.commit()

    return jsonify({'question': question, 'answer': answer})
