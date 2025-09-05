A_HotkeyInterval := 0   ; disable hotkey rate limit (infinite allowed)

; --- Remap Volume keys to Arrow keys ---
; Prevents system volume changes by blocking the native behavior

Volume_Up:: {
    Send("{Right}")
}

Volume_Down:: {
    Send("{Left}")
}
