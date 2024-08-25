class Inverter(object):
    def __new__(cls, config:dict):
        # renaming of parameters max_charge_rate -> max_grid_charge_rate
        if not 'max_grid_charge_rate' in config.keys():
            config['max_grid_charge_rate'] = config['max_charge_rate']
                        
        if config['type'].lower() == 'fronius_gen24':
            from .fronius import FroniusWR
            return FroniusWR(config['address'], config['user'], config['password'], config['max_grid_charge_rate'], config['max_pv_charge_rate'])
        elif config['type'].lower() == 'testdriver':
            from .testdriver import Testdriver
            return Testdriver(config['max_grid_charge_rate'])
        else:
            raise RuntimeError(f'[Inverter] Unkown inverter type {config["type"]}')