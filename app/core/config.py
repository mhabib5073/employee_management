from pydantic_settings import BaseSettings, SettingsConfigDict


from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-3.8-flash"

    EMPLOYEE_API_BASE_URL: str = "http://192.168.1.9:8000"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()


# class Settings(BaseSettings):
#     GEMINI_API_KEY: str
#     GEMINI_MODEL: str = "gemini-3.5-flash-lite"
#     # "gemini-3.8-flash"

#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )


# settings = Settings()