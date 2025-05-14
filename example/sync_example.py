from atlas import AtlasSync


def main():
    api = AtlasSync(grok_api_key="your_api_key")
    response = api.analyze_text(
        "Hello, Atlas!", CustomRPC="https://custom_rpc_url_here"
    )
    print(response)


if __name__ == "__main__":
    main()
