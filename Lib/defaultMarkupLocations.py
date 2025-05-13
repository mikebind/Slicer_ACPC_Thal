ANT_R = (3.8 + 5.85) / 2  # +4.82
ANT_A = -(2.1 + 6.35) / 2  # -4.225
ANT_S = (6.2 + 10.1) / 2  # +8.15
defaultCoords = {
    "LCM": (-9.0, -4.5, 1.0),
    "RCM": (9.0, -4.5, 1.0),
    "LANT": (-ANT_R, ANT_A, ANT_S),
    "RANT": (ANT_R, ANT_A, ANT_S),
    "LPUL": None,
    "RPUL": None,
}
acTemplate = {"AC": None, "PC": None, "IH": None}


def markupsFromDict(coordDict, outputMarkupsNode):
    """Create markups control points from dict where
    point labels are the keys and coords are the values.
    A None value triggers creation of a point with given
    label but unset (undefined) position.
    """
    outputMarkupsNode.RemoveAllControlPoints()
    for label, coord in coordDict.items():
        cpIdx = outputMarkupsNode.AddControlPoint(0, 0, 0, label)
        if coord is None:
            # unset the postion
            outputMarkupsNode.UnsetNthControlPointPosition(cpIdx)
        else:
            outputMarkupsNode.SetNthControlPointPositionWorld(cpIdx, *coord)
