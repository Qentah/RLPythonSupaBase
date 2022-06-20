from realtime.connection import Socket
from realtime.channel import Channel

API_KEY=${{secrets.API_KEY}}
SUPABASE_ID=${{secrets.SUPABASE_ID}}

def callback(payload):
    if payload['type'] == "DELETE" :
        print(f"PL[{payload['type']}]: {payload['old_record']}")
    else :
        print(f"PL[{payload['type']}]: {payload['record']}")

if __name__ == "__main__":
    URL = f"wss://{SUPABASE_ID}.supabase.co/realtime/v1/websocket?apikey={API_KEY}&vsn=1.0.0"
    s = Socket(URL)
    s.connect()

    channel : Channel = s.set_channel("realtime:public:machine_types")
    channel.join().on("UPDATE", callback)
    channel.join().on("INSERT", callback)
    channel.join().on("DELETE", callback)

    s.listen()
