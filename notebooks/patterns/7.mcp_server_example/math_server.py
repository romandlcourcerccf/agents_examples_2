from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calc server")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's always sunny in New York"


@mcp.tool()
async def multiply(a: int, b: int) -> int:
    """
    Multiply a and b

    Args:
      a: first int
      b: second int
    """
    print(f"--> multiply a: {a} b: {b}")
    return a * b


@mcp.tool()
async def add(a: int, b: int) -> int:
    """
    Adds a and b

    Args:
      a: first int
      b: second int
    """
    print(f"--> add a: {a} b: {b}")
    return a + b


@mcp.tool()
async def subtract(a: int, b: int) -> int:
    """
    Subtract a from b

    Args:
      a: first int
      b: second int
    """
    print(f"--> subtract a: {a} b: {b}")
    return a - b


@mcp.tool()
async def devide(a: int, b: int) -> int:
    """
    Devides a and b

    Args:
      a: first int
      b: second int
    """
    print(f"--> devide a: {a} b: {b}")
    return a / b


@mcp.tool()
async def print_result(mes: str):
    """
    Prints the result.
    """

    print(f"--> Print {mes} -->")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
