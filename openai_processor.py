import os
import qianfan

# 通过环境变量初始化认证信息
# 【推荐】使用安全认证AK/SK鉴权
# 替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk

chat_comp = qianfan.ChatCompletion(ak="yRFKBUaBN5qt0KvYFs5dwVAm", sk="XKrvxhhZpkTUwm1I3fRlX47QevK9NhdE")



def generate_summary(jina_data):
    # 生成摘要的 prompt
    prompt = '''你的任务是作为一个高级翻译和编辑，理解发给你的内容，从中生产加工输出以下信息：标题、正文、图片。确保你的响应符合以下JSON结构，准确反映提取的数据，不做修改：```json
    {
    "title": "文章标题",
    "content": "文章摘要",
    "image": "文章包含的图片链接，保留url，如果没有留空"
    }
```重要的是你的输出严格遵守这种格式。
    -严格确保统一翻译为中文
    -不翻译公司名称、人名    '''

    # 进行多轮对话
    resp = chat_comp.do(model="ERNIE-4.0-8K", messages=[
        {
            "role": "user",
            "content": f"{prompt}{jina_data}"
        }
    ])

    # 输出响应结果
    print(resp["body"])

    # 返回响应中的结果
    return resp


# 示例调用 generate_summary 函数
jina_data = "这是输入的内容，需要进行摘要生成。"
response = generate_summary(jina_data)
