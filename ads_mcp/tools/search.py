import os
from ads_mcp.tools.api import execute_gaql_core

def search(customer_id, fields, resource, conditions=None, login_customer_id=None):
    """
    Executes a search query against the Google Ads API.
    
    Args:
        customer_id: The customer ID to query.
        fields: List of fields to select.
        resource: The resource to query.
        conditions: List of WHERE conditions.
        login_customer_id: Optional login customer ID (MCC).
        
    Returns:
        List of result rows as dictionaries.
    """
    query = f"SELECT {', '.join(fields)} FROM {resource}"
    if conditions:
        query += f" WHERE {' AND '.join(conditions)}"
        
    # Check env var for login_customer_id if not provided
    if not login_customer_id:
        login_customer_id = os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID")
        
    return execute_gaql_core(query=query, customer_id=customer_id, login_customer_id=login_customer_id)
