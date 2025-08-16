import dotenv


# 定义一个配置类

class Config:
    def __init__(self):
        self.config = dotenv.dotenv_values(".env")
        self.DEEPSEEK_API_KEY = self.config.get("DEEPSEEK_API_KEY")
        self.LANGSMITH_API_KEY = self.config.get("LANGSMITH_API_KEY")
        self.LANGSMITH_TRACING = self.config.get("LANGSMITH_TRACING")
        self.LANGSMITH_ENDPOINT = self.config.get("LANGSMITH_ENDPOINT")
        self.LANGSMITH_PROJECT = self.config.get("LANGSMITH_PROJECT")