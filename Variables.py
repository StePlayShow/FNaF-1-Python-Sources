class Vars:

    # 0..2 - MainMenu
    # 3 - WarningScene
    # 4..5 - Newspaper
    # 6 - LoadingScene
    # 7 - NextDay

    # Other vars

    CursorPos: tuple[int, int] = (0, 0)
    CursorPosX: int = 0
    CursorPosY: int = 0
    Frames: int = 0
    Opacity: list[int] = [255, 255, 0, 0, 0, 0, 255, 0, 0, 255, 0, 0, 255]
    dTime: float = 1

    # MainMenu vars

    RandomNum: int = 0
    Visibility: int = 0
    Y1: int = -33
    OptionNumber: int = 0
    OptionNumber1: int = 0
    OptionNumber2: int = 0
    OptionNumber3: int = 0
    OptionNumber4: int = 0
    OptionNumber5: int = 0
    start_ticks: int = 0
    Extra: bool = False
    CheatsOption: bool = False
    DMOption: bool = False

    FastNight: bool = False
    Radar: bool = False
    EndlessPower: bool = False
    LongNight: bool = False
    Aggrmode: bool = False
    Darkmode: bool = False

    # LoadingScene vars

    # Nightshift vars

    HourLength: int = 90 # 90
    X1: int = 0
    X2: int = 0
    IndicatorX2: int = 0
    IntervalX2: int = 0
    LeftDoorIsClosed: bool = False
    RightDoorIsClosed: bool = False
    LeftLightIsOn: bool = False
    RightLightIsOn: bool = False
    LeftDoorIsMoving: bool = False
    RightDoorIsMoving: bool = False
    LeftButtonsAreBroken: bool = False
    RightButtonsAreBroken: bool = False
    CameraIsOn: bool = False
    TabletIsUsing: bool = False
    TabletIsMoving: bool = False
    AbleToUseTablet: bool = True
    FreddyActivity: int = 0
    BonnyActivity: int = 0
    ChicaActivity: int = 0
    FoxyActivity: int = 0
    FreddyPosition: str = '1a'
    BonnyPosition: str = '1a'
    ChicaPosition: str = '1a'
    FoxyPosition: int = 0
    FreddyVars: list[int] = [0, 0, 0]
    BonnyVars: list[int] = [1, 0, 1, 0]
    ChicaVars: list[int] = [1, 0, 1, 0]
    FoxyVars: list[int] = [0, 0, 0, 0, 0]
    GoldenFreddyVars: list[int] = [0, 0, 0, 0]
    FreddyJumpscare: bool = False
    BonnyJumpscare: bool = False
    ChicaJumpscare: bool = False
    FoxyJumpscare: bool = False
    ReadyToJumpscare: bool = False
    JumpscareVars: list[int] = [10, 40]
    HallucinationVars: list[int] = [0, 0, 0, 0]
    RandomNum1: int = 0
    RandomNum2: int = 0
    RandomNum3: int = 0
    RandomForPic: int = 1
    Hour: int = 0
    Power: int = 999
    Usage: int = 1
    PowerDown: bool = False
    PowerDownVars: list[int] = [0, 0, 0, 0]
    CallIsMuted: bool = False
    NoSignalVars: list[int] = [0, 0]
    ControlRoom: list[int] = [False, False, False, False, False]
    Camera: dict = {'1a': True, '1b': False, '1c': False, '2a': False, '2b': False, '3': False,
                        '4a': False, '4b': False, '5': False, '6': False, '7': False}

    # Gameover vars

    RandomNum4: int = 0

    # NextDay vars

    Y2: float = 0

    # Customize vars

    FreddyAI: int = 1
    BonnyAI: int = 3
    ChicaAI: int = 3
    FoxyAI: int = 1

    # Data vars

    Night: int = 1
    BeatGame: bool = False
    Beat6: bool = False
    Beat7: bool = False
    BeatHardMode: bool = False