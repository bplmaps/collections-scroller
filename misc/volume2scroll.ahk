#MaxHotkeysPerInterval 0   ; disable hotkey rate limit (infinite allowed)

; --- Remap Volume keys to Arrow keys ---
; Prevents system volume changes by blocking the native behavior

; Volume Up -> Right Arrow
Volume_Up::
    Send {Right}
return

; Volume Down -> Left Arrow
Volume_Down::
    Send {Left}
return
