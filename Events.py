from Variables import Vars

_events_every = {}
_events_once = {}
_events_once_event = {}


def Every(timer: float, interval: int | float, number: int, strict: bool = False) -> bool:
    """
    :param timer:
        value of self.time of scene
    :param interval:
        in seconds
    :param number:
        number of event
    :return:
        True if timer every time reach interval, else return False
    """
    global _events_every
    n = _events_every.get(f'{interval}n{number}')
    if n is None:
        _events_every[f'{interval}n{number}'] = [Vars.Frames, (timer // interval) + 1]
        n = _events_every[f'{interval}n{number}']
    elif Vars.Frames != n[0]:
        _events_every[f'{interval}n{number}'] = [Vars.Frames, n[1]]
    elif not strict:
        raise KeyError(f"Event with this key ({interval}n{number}) already exist")

    if timer > interval * n[1]:
        _events_every[f'{interval}n{number}'] = [Vars.Frames, (timer // interval) + 1]
        return True
    return False


def Once(timer: float, time: int | float, number: int, strict: bool = False) -> bool:
    """
    :param timer:
        value of self.time of scene
    :param time:
        in seconds
    :param number:
         number of event
    :return:
        True if timer reach time, else return False
    """
    global _events_once
    n = _events_once.get(f'{time}n{number}')
    if n is None:
        n = [Vars.Frames, timer > time]
        _events_once[f'{time}n{number}'] = n
    elif n[1]:
        return False
    elif Vars.Frames != n[0]:
        _events_once[f'{time}n{number}'] = [Vars.Frames, n[1]]
    elif not strict:
        raise KeyError(f"Event with this key ({time}n{number}) already exist")

    if timer > time and not n[1]:
        _events_once[f'{time}n{number}'] = [Vars.Frames, timer > time]
        return True
    return False


def OnceEvent(number: int, resume: bool = True, strict: bool = False) -> bool:
    """
    This function allows for the execution of the code to occur only once
    during the fulfillment of the conditions. Therefore, it is crucial to place
    this approach at the end of the if statement's conditions. Additionally, if
    the resumable parameter is set to False, the method will only return
    True once while the conditions are met and cannot be restarted if the
    conditions are met again.

    :param number:
         number of event
    :param resume:
         yes
    :return:
        True or False
    """
    global _events_once_event
    n = _events_once_event.get(f'{number}')
    if n is None:
        _events_once_event[f'{number}'] = Vars.Frames
        return True
    elif Vars.Frames != n:
        if Vars.Frames - n == 1:
            _events_once_event[f'{number}'] = Vars.Frames
            return False
        elif resume:
            _events_once_event[f'{number}'] = Vars.Frames
            return True
    elif not strict:
        raise KeyError(f"Event with this key ({number}) already exist")

def ClearEvents():
    global _events_every, _events_once, _events_once_event
    _events_every = {}
    _events_once = {}
    _events_once_event = {}