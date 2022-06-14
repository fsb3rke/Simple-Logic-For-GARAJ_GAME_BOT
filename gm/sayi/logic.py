import json

def msg(content: str): # TODO: BURAYI KENDINE GORE AYARLARSIN HER MESAJ GELDIĞINDE OLUCAK
    try:
        m_content = int(content)
        with open("last.number.json", "r") as f:
            json_last_number = json.loads(f.read())
            last_number = json_last_number["last_number"]
        if m_content == last_number+1:
            with open("last.number.json", "w") as f:
                json_last_number["last_number"] = m_content
                dump_last_number = json.dumps(json_last_number)
                f.write(dump_last_number)
            if m_content%100 == 0:
                # TODO: BOT MESAJ GONDERSIN 100 KATI OLUNCA
                pass
        else:
            # TODO: MESAJI SİLSİN
            pass
    except ValueError:
        pass
