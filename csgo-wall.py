import pymem                   # pip install pymem
import pymem.process           
import requests                # pip install requests
from threading import Thread   


print ('>>> Starting csgo python cheat...')

pm = pymem.Pymem("csgo.exe")                                                   
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

print ('')
print ('>>> Getting offset...')

offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(offsets).json()

dwGlowObjectManager = int(response["signatures"]["dwGlowObjectManager"])
dwEntityList = int(response["signatures"]["dwEntityList"])

m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
m_iGlowIndex = int(response["netvars"]["m_iGlowIndex"])

print ('>>> Starting WallHack...')


def ESP():
    while True:
        glow_manager = pm.read_int(client + dwGlowObjectManager)

        for i in range(1, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                if entity_team_id == 2:  # Terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)

                elif entity_team_id == 3:  # Counter-terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)

Thread(target=ESP).start()

print ('>>> Cheat activated!')