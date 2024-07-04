\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  121.46 opening_links[0] + 117.41 opening_links[1]
   + 131.93 opening_links[2] + 4.275371328902321 trucks_started[0]
   + 4.275371328902321 trucks_started[1]
   + 4.275371328902321 trucks_started[2]
   + 4.275371328902321 trucks_started[3]
   + 4.275371328902321 trucks_started[4]
   + 4.275371328902321 trucks_started[5]
   + 4.275371328902321 trucks_started[6]
   + 4.275371328902321 trucks_started[7]
   + 5.885847432613251 trucks_started[8]
   + 5.885847432613251 trucks_started[9]
   + 5.885847432613251 trucks_started[10]
   + 5.885847432613251 trucks_started[11]
   + 5.885847432613251 trucks_started[12]
   + 5.885847432613251 trucks_started[13]
   + 5.885847432613251 trucks_started[14]
   + 5.885847432613251 trucks_started[15]
   + 5.107837115648854 trucks_started[16]
   + 5.107837115648854 trucks_started[17]
   + 5.107837115648854 trucks_started[18]
   + 5.107837115648854 trucks_started[19]
   + 5.107837115648854 trucks_started[20]
   + 5.107837115648854 trucks_started[21]
   + 5.107837115648854 trucks_started[22]
   + 5.107837115648854 trucks_started[23] + 0.2021 inventory[0]
   + 0.2021 inventory[1] + 0.2021 inventory[2] + 0.2021 inventory[3]
   + 0.2021 inventory[4] + 0.2021 inventory[5] + 0.2021 inventory[6]
   + 0.2021 inventory[7] + 2.575 early_delivery[0]
   + 2.575 early_delivery[1] + 2.575 early_delivery[2]
   + 2.575 early_delivery[3] + 2.575 early_delivery[4]
   + 2.575 early_delivery[5] + 2.575 early_delivery[6]
   + 51.5 early_delivery[7] + 5.15 late_delivery[0] + 5.15 late_delivery[1]
   + 5.15 late_delivery[2] + 5.15 late_delivery[3] + 5.15 late_delivery[4]
   + 5.15 late_delivery[5] + 5.15 late_delivery[6] + 51.5 late_delivery[7]
   + 10.43 link_capacity[0] + 9.42 link_capacity[1] + 6.99 link_capacity[2]
   + 0 total_stored_depot[0] + 0 total_stored_depot[1]
   + 0 total_stored_depot[2] + 0 total_stored_depot[3]
   + 0 total_stored_depot[4] + 0 total_stored_depot[5]
   + 0 total_stored_depot[6] + 0 total_stored_depot[7]
   + 0 total_delivered[0] + 0 total_delivered[1] + 0 total_delivered[2]
   + 0 total_delivered[3] + 0 total_delivered[4] + 0 total_delivered[5]
   + 0 total_delivered[6] + 0 total_delivered[7]
Subject To
 R0: inventory[0] = 0
 R1: outgoing_depots[0] = 0
 R2: - products_shipped[17] + outgoing_depots[1] = 0
 R3: - products_shipped[18] + outgoing_depots[2] = 0
 R4: - products_shipped[19] + outgoing_depots[3] = 0
 R5: - products_shipped[20] + outgoing_depots[4] = 0
 R6: - products_shipped[21] + outgoing_depots[5] = 0
 R7: - products_shipped[22] + outgoing_depots[6] = 0
 R8: - products_shipped[23] + outgoing_depots[7] = 0
 R9: incoming_depots[0] = 0
 R10: incoming_depots[1] = 0
 R11: incoming_depots[1] = 0
 R12: - products_shipped[0] + incoming_depots[2] = 0
 R13: - products_shipped[1] + incoming_depots[3] = 0
 R14: - products_shipped[2] + incoming_depots[4] = 0
 R15: - products_shipped[3] + incoming_depots[5] = 0
 R16: - products_shipped[4] + incoming_depots[6] = 0
 R17: - products_shipped[5] + incoming_depots[7] = 0
 R18: inventory[0] = 0
 R19: - inventory[0] + inventory[1] + outgoing_depots[1]
   - incoming_depots[1] = 0
 R20: - inventory[1] + inventory[2] + outgoing_depots[2]
   - incoming_depots[2] = 0
 R21: - inventory[2] + inventory[3] + outgoing_depots[3]
   - incoming_depots[3] = 0
 R22: - inventory[3] + inventory[4] + outgoing_depots[4]
   - incoming_depots[4] = 0
 R23: - inventory[4] + inventory[5] + outgoing_depots[5]
   - incoming_depots[5] = 0
 R24: - inventory[5] + inventory[6] + outgoing_depots[6]
   - incoming_depots[6] = 0
 R25: - inventory[6] + inventory[7] + outgoing_depots[7]
   - incoming_depots[7] = 0
 R26: arriving_trucks[0] = 0
 R27: arriving_trucks[1] = 0
 R28: - trucks_started[0] + arriving_trucks[2] = 0
 R29: - trucks_started[1] + arriving_trucks[3] = 0
 R30: - trucks_started[2] + arriving_trucks[4] = 0
 R31: - trucks_started[3] + arriving_trucks[5] = 0
 R32: - trucks_started[4] + arriving_trucks[6] = 0
 R33: - trucks_started[5] + arriving_trucks[7] = 0
 R34: arriving_trucks[8] = 0
 R35: arriving_trucks[9] = 0
 R36: - trucks_started[8] + arriving_trucks[10] = 0
 R37: - trucks_started[9] + arriving_trucks[11] = 0
 R38: - trucks_started[10] + arriving_trucks[12] = 0
 R39: - trucks_started[11] + arriving_trucks[13] = 0
 R40: - trucks_started[12] + arriving_trucks[14] = 0
 R41: - trucks_started[13] + arriving_trucks[15] = 0
 R42: arriving_trucks[16] = 0
 R43: arriving_trucks[17] = 0
 R44: arriving_trucks[18] = 0
 R45: - trucks_started[16] + arriving_trucks[19] = 0
 R46: - trucks_started[17] + arriving_trucks[20] = 0
 R47: - trucks_started[18] + arriving_trucks[21] = 0
 R48: - trucks_started[19] + arriving_trucks[22] = 0
 R49: - trucks_started[20] + arriving_trucks[23] = 0
 R50: - products_shipped[0] - products_shipped[16] + total_shipped[0] = 0
 R51: - products_shipped[1] - products_shipped[17] + total_shipped[1] = 0
 R52: - products_shipped[2] - products_shipped[18] + total_shipped[2] = 0
 R53: - products_shipped[3] - products_shipped[19] + total_shipped[3] = 0
 R54: - products_shipped[4] - products_shipped[20] + total_shipped[4] = 0
 R55: - products_shipped[5] - products_shipped[21] + total_shipped[5] = 0
 R56: - products_shipped[6] - products_shipped[22] + total_shipped[6] = 0
 R57: - products_shipped[7] - products_shipped[23] + total_shipped[7] = 0
 R58: produced[0] - total_shipped[0] <= 0
 R59: - 5 produced[0] + total_shipped[0] <= 0
 R60: produced[1] - total_shipped[1] <= 0
 R61: - 5 produced[1] + total_shipped[1] <= 0
 R62: produced[2] - total_shipped[2] <= 0
 R63: - 5 produced[2] + total_shipped[2] <= 0
 R64: produced[3] - total_shipped[3] <= 0
 R65: - 5 produced[3] + total_shipped[3] <= 0
 R66: produced[4] - total_shipped[4] <= 0
 R67: - 5 produced[4] + total_shipped[4] <= 0
 R68: produced[5] - total_shipped[5] <= 0
 R69: - 5 produced[5] + total_shipped[5] <= 0
 R70: produced[6] - total_shipped[6] <= 0
 R71: - 5 produced[6] + total_shipped[6] <= 0
 R72: produced[7] - total_shipped[7] <= 0
 R73: - 5 produced[7] + total_shipped[7] <= 0
 R74: - 100000 opening_links[0] + products_shipped[0] <= 0
 R75: - 100000 opening_links[0] + products_shipped[1] <= 0
 R76: - 100000 opening_links[0] + products_shipped[2] <= 0
 R77: - 100000 opening_links[0] + products_shipped[3] <= 0
 R78: - 100000 opening_links[0] + products_shipped[4] <= 0
 R79: - 100000 opening_links[0] + products_shipped[5] <= 0
 R80: - 100000 opening_links[0] + products_shipped[6] <= 0
 R81: - 100000 opening_links[0] + products_shipped[7] <= 0
 R82: - 100000 opening_links[1] + products_shipped[8] <= 0
 R83: - 100000 opening_links[1] + products_shipped[9] <= 0
 R84: - 100000 opening_links[1] + products_shipped[10] <= 0
 R85: - 100000 opening_links[1] + products_shipped[11] <= 0
 R86: - 100000 opening_links[1] + products_shipped[12] <= 0
 R87: - 100000 opening_links[1] + products_shipped[13] <= 0
 R88: - 100000 opening_links[1] + products_shipped[14] <= 0
 R89: - 100000 opening_links[1] + products_shipped[15] <= 0
 R90: - 100000 opening_links[2] + products_shipped[16] <= 0
 R91: - 100000 opening_links[2] + products_shipped[17] <= 0
 R92: - 100000 opening_links[2] + products_shipped[18] <= 0
 R93: - 100000 opening_links[2] + products_shipped[19] <= 0
 R94: - 100000 opening_links[2] + products_shipped[20] <= 0
 R95: - 100000 opening_links[2] + products_shipped[21] <= 0
 R96: - 100000 opening_links[2] + products_shipped[22] <= 0
 R97: - 100000 opening_links[2] + products_shipped[23] <= 0
 R98: - products_shipped[0] - products_shipped[16]
   + total_shipped_depots[0] = 0
 R99: - products_shipped[1] - products_shipped[17]
   + total_shipped_depots[1] = 0
 R100: - products_shipped[2] - products_shipped[18]
   + total_shipped_depots[2] = 0
 R101: - products_shipped[3] - products_shipped[19]
   + total_shipped_depots[3] = 0
 R102: - products_shipped[4] - products_shipped[20]
   + total_shipped_depots[4] = 0
 R103: - products_shipped[5] - products_shipped[21]
   + total_shipped_depots[5] = 0
 R104: - products_shipped[6] - products_shipped[22]
   + total_shipped_depots[6] = 0
 R105: - products_shipped[7] - products_shipped[23]
   + total_shipped_depots[7] = 0
 R106: - inventory[0] + total_shipped_depots[0] <= 0
 R107: - inventory[1] + total_shipped_depots[1] <= 0
 R108: - inventory[2] + total_shipped_depots[2] <= 0
 R109: - inventory[3] + total_shipped_depots[3] <= 0
 R110: - inventory[4] + total_shipped_depots[4] <= 0
 R111: - inventory[5] + total_shipped_depots[5] <= 0
 R112: - inventory[6] + total_shipped_depots[6] <= 0
 R113: - inventory[7] + total_shipped_depots[7] <= 0
 R114: - 100000 opening_links[0] + link_capacity[0] <= 0
 R115: - 100000 opening_links[1] + link_capacity[1] <= 0
 R116: - 100000 opening_links[2] + link_capacity[2] <= 0
 R117: trucks_started[0] - link_capacity[0] <= 0
 R118: trucks_started[1] - link_capacity[0] <= 0
 R119: trucks_started[2] - link_capacity[0] <= 0
 R120: trucks_started[3] - link_capacity[0] <= 0
 R121: trucks_started[4] - link_capacity[0] <= 0
 R122: trucks_started[5] - link_capacity[0] <= 0
 R123: trucks_started[6] - link_capacity[0] <= 0
 R124: trucks_started[7] - link_capacity[0] <= 0
 R125: trucks_started[8] - link_capacity[1] <= 0
 R126: trucks_started[9] - link_capacity[1] <= 0
 R127: trucks_started[10] - link_capacity[1] <= 0
 R128: trucks_started[11] - link_capacity[1] <= 0
 R129: trucks_started[12] - link_capacity[1] <= 0
 R130: trucks_started[13] - link_capacity[1] <= 0
 R131: trucks_started[14] - link_capacity[1] <= 0
 R132: trucks_started[15] - link_capacity[1] <= 0
 R133: trucks_started[16] - link_capacity[2] <= 0
 R134: trucks_started[17] - link_capacity[2] <= 0
 R135: trucks_started[18] - link_capacity[2] <= 0
 R136: trucks_started[19] - link_capacity[2] <= 0
 R137: trucks_started[20] - link_capacity[2] <= 0
 R138: trucks_started[21] - link_capacity[2] <= 0
 R139: trucks_started[22] - link_capacity[2] <= 0
 R140: trucks_started[23] - link_capacity[2] <= 0
 R141: 0.47 inventory[0] <= 12.97
 R142: 0.47 inventory[1] <= 12.97
 R143: 0.47 inventory[2] <= 12.97
 R144: 0.47 inventory[3] <= 12.97
 R145: 0.47 inventory[4] <= 12.97
 R146: 0.47 inventory[5] <= 12.97
 R147: 0.47 inventory[6] <= 12.97
 R148: 0.47 inventory[7] <= 12.97
 R149: 0.47 products_shipped[0] - 1.44 trucks_started[0] <= 0
 R150: 0.47 products_shipped[1] - 1.44 trucks_started[1] <= 0
 R151: 0.47 products_shipped[2] - 1.44 trucks_started[2] <= 0
 R152: 0.47 products_shipped[3] - 1.44 trucks_started[3] <= 0
 R153: 0.47 products_shipped[4] - 1.44 trucks_started[4] <= 0
 R154: 0.47 products_shipped[5] - 1.44 trucks_started[5] <= 0
 R155: 0.47 products_shipped[6] - 1.44 trucks_started[6] <= 0
 R156: 0.47 products_shipped[7] - 1.44 trucks_started[7] <= 0
 R157: 0.47 products_shipped[8] - 1.44 trucks_started[8] <= 0
 R158: 0.47 products_shipped[9] - 1.44 trucks_started[9] <= 0
 R159: 0.47 products_shipped[10] - 1.44 trucks_started[10] <= 0
 R160: 0.47 products_shipped[11] - 1.44 trucks_started[11] <= 0
 R161: 0.47 products_shipped[12] - 1.44 trucks_started[12] <= 0
 R162: 0.47 products_shipped[13] - 1.44 trucks_started[13] <= 0
 R163: 0.47 products_shipped[14] - 1.44 trucks_started[14] <= 0
 R164: 0.47 products_shipped[15] - 1.44 trucks_started[15] <= 0
 R165: 0.47 products_shipped[16] - 1.44 trucks_started[16] <= 0
 R166: 0.47 products_shipped[17] - 1.44 trucks_started[17] <= 0
 R167: 0.47 products_shipped[18] - 1.44 trucks_started[18] <= 0
 R168: 0.47 products_shipped[19] - 1.44 trucks_started[19] <= 0
 R169: 0.47 products_shipped[20] - 1.44 trucks_started[20] <= 0
 R170: 0.47 products_shipped[21] - 1.44 trucks_started[21] <= 0
 R171: 0.47 products_shipped[22] - 1.44 trucks_started[22] <= 0
 R172: 0.47 products_shipped[23] - 1.44 trucks_started[23] <= 0
Bounds
Binaries
 opening_links[0] opening_links[1] opening_links[2] produced[0] produced[1]
 produced[2] produced[3] produced[4] produced[5] produced[6] produced[7]
Generals
 trucks_started[0] trucks_started[1] trucks_started[2] trucks_started[3]
 trucks_started[4] trucks_started[5] trucks_started[6] trucks_started[7]
 trucks_started[8] trucks_started[9] trucks_started[10] trucks_started[11]
 trucks_started[12] trucks_started[13] trucks_started[14]
 trucks_started[15] trucks_started[16] trucks_started[17]
 trucks_started[18] trucks_started[19] trucks_started[20]
 trucks_started[21] trucks_started[22] trucks_started[23] link_capacity[0]
 link_capacity[1] link_capacity[2] arriving_trucks[0] arriving_trucks[1]
 arriving_trucks[2] arriving_trucks[3] arriving_trucks[4]
 arriving_trucks[5] arriving_trucks[6] arriving_trucks[7]
 arriving_trucks[8] arriving_trucks[9] arriving_trucks[10]
 arriving_trucks[11] arriving_trucks[12] arriving_trucks[13]
 arriving_trucks[14] arriving_trucks[15] arriving_trucks[16]
 arriving_trucks[17] arriving_trucks[18] arriving_trucks[19]
 arriving_trucks[20] arriving_trucks[21] arriving_trucks[22]
 arriving_trucks[23]
End
