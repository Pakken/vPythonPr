import json

def main():

    with open('solar_system_view_data.txt',mode='r') as old_data:
        with open('solar_system_vdata',mode='w') as new_data:
            c = {}
            for i in old_data:
                a,b = i.split(':',1)
                c.update({a.strip('(') : dict(tuple(j.replace('(',' ').replace(')',' ').strip().split(':')) for j in (b.split(',')))})
            c = json.dumps(c)
            new_data.write(c)             
if __name__ == '__main__':
    main()
