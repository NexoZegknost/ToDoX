from supabase import create_client, Client

url: str = "https://qeyqxsmezoaeqhzitils.supabase.co"
key: str = "sb_publishable_wcHGuXxto7CjLtaaU6MVvg__GNhGP1O"
SUPABASE: Client = create_client(url, key)
