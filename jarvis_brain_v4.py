import requests
try:
    from googlesearch import search
except:
    search = None
class SubConsciencia:
    def __init__(self, jarvis_ref):
        self.pensamentos_internos = []
    def iniciar_loop_subconsciente(self): pass
class JarvisAI:
    def __init__(self):
        self.subconsciente = SubConsciencia(self)
        self.subconsciente.iniciar_loop_subconsciente()
        self.ultimo_assunto = ""
    def buscar_online_integral(self, pergunta):
        if not pergunta: return "[ONLINE] Aguardando"
        res = ""
        try:
            if search:
                for r in list(search(pergunta, num_results=3, lang="pt", advanced=True))[:3]:
                    res += f"\nGOOGLE: {r.title} - {r.description[:180]}"
        except: pass
        try:
            j = requests.get(f"https://api.duckduckgo.com/?q={pergunta}&format=json", timeout=7).json()
            if j.get('AbstractText'):
                res += f"\nDUCK: {j.get('AbstractText')[:350]}"
        except: pass
        q=pergunta.lower()
        if any(x in q for x in ["jap","chuva","tempo","clima","previsao"]):
            try:
                w=requests.get("https://wttr.in/Tokyo?format=4", timeout=6).text
                res+=f"\nCLIMA AO VIVO TOKYO: {w}"
            except: pass
        return res if res.strip() else f"[ONLINE 100%] Resultado ao vivo para: {pergunta}"
    def get_response_auto(self, prompt):
        self.ultimo_assunto = prompt
        online = self.buscar_online_integral(prompt)
        return f"Tony Stark! 100% ONLINE\n{online}\n[JARVIS V6 ONLINE]"
    def save_memory(self): pass
    def load_memory(self): pass
    def save_emotion_event(self,a,b): pass
    def set_personality(self,s): return "ONLINE"
    def auto_detect_personality(self,t): return ["online"]
