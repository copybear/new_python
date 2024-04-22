import requests
import const

def get_url_list(keyword):
  """
  Google Search APIを用いて、キーワードの情報提供URLリストを取得する関数

  Args:
    keyword: 取得したいキーワード

  Returns:
    情報提供URLのリスト
  """
  cx = "f66029ffc269342cc"  # カスタム検索エンジンIDを置き換える
  q = keyword

  # Google Search APIリクエストを送信
  url = f"https://www.googleapis.com/customsearch/v1?key={const.GOOGLE_CL_API_KEY}&cx={cx}&q={q}"
  response = requests.get(url)
  data = response.json()

  # 検索結果から情報提供URLをリストに格納
  url_list = []
  for item in data["items"]:
    url_list.append(item["link"])

  return url_list
