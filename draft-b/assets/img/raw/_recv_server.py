# 画像受信用の簡易HTTPサーバー（Gemini blob画像をブラウザからPOSTで受け取る）
# 使い方: python _recv_server.py → http://127.0.0.1:8970/save/<name> にbase64データURLをPOST
import base64
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

SAVE_DIR = r"D:\たぶんごみ\ClaudeCODE\web\draft-b\assets\img\raw"

class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        # どのオリジンからでも受け付ける（ローカル一時用途のみ）
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "content-type")

    def do_OPTIONS(self):
        # CORSプリフライトに応答
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        try:
            # パスからファイル名を取得（英数字とドット・ハイフンのみ許可）
            m = re.match(r"^/save/([A-Za-z0-9._-]+)$", self.path)
            if not m:
                self.send_response(400); self._cors(); self.end_headers(); return
            name = m.group(1)
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            # data URL形式（data:image/jpeg;base64,...）からbase64部分を取り出す
            if "," in body:
                body = body.split(",", 1)[1]
            data = base64.b64decode(body)
            with open(SAVE_DIR + "\\" + name, "wb") as f:
                f.write(data)
            self.send_response(200)
            self._cors()
            self.end_headers()
            self.wfile.write(b"OK")
            print(f"saved: {name} ({len(data)} bytes)")
        except Exception as e:
            # エラー時も応答を返す
            print(f"error: {e}")
            self.send_response(500); self._cors(); self.end_headers()

    def log_message(self, *args):
        pass  # アクセスログは抑制

if __name__ == "__main__":
    print("listening on 127.0.0.1:8970")
    HTTPServer(("127.0.0.1", 8970), Handler).serve_forever()
