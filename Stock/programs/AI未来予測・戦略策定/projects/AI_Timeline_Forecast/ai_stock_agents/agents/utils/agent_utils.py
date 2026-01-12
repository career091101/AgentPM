# AI Stock Agents - Agent Utilities
# Based on TradingAgents-main/tradingagents/agents/utils/agent_utils.py

from langchain_core.messages import HumanMessage, RemoveMessage


def create_msg_delete():
    """
    Create a message deletion function for clearing tool-calling history.

    This is used after each analyst completes their tool-calling loop
    to avoid context overflow from accumulated tool messages.

    Returns:
        function: Message deletion function
    """

    def delete_messages(state):
        """Clear messages and add placeholder for Anthropic compatibility"""
        messages = state["messages"]

        # Remove all messages
        removal_operations = [RemoveMessage(id=m.id) for m in messages]

        # Add a minimal placeholder message
        placeholder = HumanMessage(content="Continue")

        return {"messages": removal_operations + [placeholder]}

    return delete_messages
