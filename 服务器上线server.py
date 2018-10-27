
import logging
import json
from music_model import predict as music_pr
from social_model import predict as social_pr
from phone_model import predict as phone_pr
from map_model import predict as map_pr
from flask import Flask, jsonify, request

#导入模型里的预测函数，预测函数已经有输出格式了
logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)
def social_predict(query):
    result= social_pr(query)
    return json.dumps(result, ensure_ascii=False)

def music_predict(query):
    result= music_pr(query)
    return json.dumps(result, ensure_ascii=False)

def phone_predict(query):
    result= phone_pr(query)
    return json.dumps(result, ensure_ascii=False)

def map_predict(query):
    result= map_pr(query)
    return json.dumps(result, ensure_ascii=False)

# @app.route('/index', methods=["POST","GET"])
# def index():
#     return "tensorflow"

#最终生成接口的postman网址是 http://172.25.24.226:17654/intention_slot

@app.route('/intention_slot', methods=["POST","GET"])  
def get_classification():
    print("--------------------")
    # return "tensorflow"
#query和scene为接口里的两个输入参数
    if request.method=="POST":
        if 'query' not in request.form or "scene" not in request.form :
            return jsonify(message='Parameter missed', code=404)
        else:
            session = request.form
            logging.info('The session is {}'.format(session))
            try:
                logging.info('---------------------processing scene classification-------------------------')
                logging.info("session is {}".format(session))
                # query = request.form['query']
                # scene = request.form['scene']
                query = session.get("query", None)
                scene = session.get("scene", None)
                print(scene)
                if scene == "map":
                    return map_predict(query)
                elif scene == "social":
                    return social_predict(query)
                elif scene == "phone":
                    return phone_predict(query)
                else:
                    return music_predict(query)
                logging.info("result is {}".format(result))
            except Exception as e:
                return jsonify(code=1, message=repr(e))

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=17654)

#上线输出的数据格式
result = dict()

result["intent"] = pred_intent
result["intent_score"] = str(max_intent_score)
result["slot"] = pred_slot
result["slot_score"] = str(max_slot_score)

res = dict()
res["code"] = 0
res["data"] = result
res["message"] = "ok"
