#!/usr/bin/env python3

# This code toggles output of the Rigol DP800 series PSU.

# config
sup_ip = "192.168.1.50" # Where is your PSU?
sup_ch = "CH1"          # Which channel you want to toggle?

# init
import vxi11
sup = vxi11.Instrument(sup_ip)

# show device identity
sup_ident = sup.ask("*IDN?")
print(sup_ip + " is \"" + sup_ident + "\"")

# toggle channel
sup_ch_sts = sup.ask(":OUTP? " + sup_ch)
if sup_ch_sts == "ON":
    sup.write(":OUTP " + sup_ch + ",OFF")
else:
    sup.write(":OUTP " + sup_ch + ",ON")

# show channel state
sup_ch_sts = sup.ask(":OUTP? CH1")
print(sup_ch + " is " + sup_ch_sts)
