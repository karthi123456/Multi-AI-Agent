from dotenv import load_dotenv

load_dotenv()

from crew import stock_crew  # noqa: E402  (must import after load_dotenv)

def run(stock: str):
    result = stock_crew.kickoff(inputs={"stock": stock})
    print(result)


if __name__ == "__main__":
    run("TESLA")
    # run("APPLE")
