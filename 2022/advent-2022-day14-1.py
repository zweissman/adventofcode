DATA_TEST = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]
DATA = [
    "527,49 -> 527,51 -> 523,51 -> 523,55 -> 536,55 -> 536,51 -> 531,51 -> 531,49",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "538,67 -> 542,67",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "527,148 -> 532,148",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "523,46 -> 527,46",
    "508,27 -> 508,29 -> 503,29 -> 503,35 -> 512,35 -> 512,29 -> 510,29 -> 510,27",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "548,104 -> 548,105 -> 559,105 -> 559,104",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "517,46 -> 521,46",
    "514,152 -> 519,152",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "522,80 -> 522,75 -> 522,80 -> 524,80 -> 524,71 -> 524,80 -> 526,80 -> 526,77 -> 526,80",
    "541,64 -> 545,64",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "548,104 -> 548,105 -> 559,105 -> 559,104",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "527,49 -> 527,51 -> 523,51 -> 523,55 -> 536,55 -> 536,51 -> 531,51 -> 531,49",
    "491,155 -> 491,157 -> 490,157 -> 490,160 -> 501,160 -> 501,157 -> 497,157 -> 497,155",
    "514,40 -> 518,40",
    "527,49 -> 527,51 -> 523,51 -> 523,55 -> 536,55 -> 536,51 -> 531,51 -> 531,49",
    "508,27 -> 508,29 -> 503,29 -> 503,35 -> 512,35 -> 512,29 -> 510,29 -> 510,27",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "510,140 -> 510,141 -> 521,141 -> 521,140",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "529,89 -> 534,89",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "499,19 -> 499,21 -> 497,21 -> 497,24 -> 508,24 -> 508,21 -> 505,21 -> 505,19",
    "521,85 -> 526,85",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "508,27 -> 508,29 -> 503,29 -> 503,35 -> 512,35 -> 512,29 -> 510,29 -> 510,27",
    "535,58 -> 539,58",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "526,67 -> 530,67",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "532,67 -> 536,67",
    "544,67 -> 548,67",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "538,61 -> 542,61",
    "525,87 -> 530,87",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "513,148 -> 518,148",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "508,44 -> 512,44",
    "499,19 -> 499,21 -> 497,21 -> 497,24 -> 508,24 -> 508,21 -> 505,21 -> 505,19",
    "527,49 -> 527,51 -> 523,51 -> 523,55 -> 536,55 -> 536,51 -> 531,51 -> 531,49",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "528,152 -> 533,152",
    "522,80 -> 522,75 -> 522,80 -> 524,80 -> 524,71 -> 524,80 -> 526,80 -> 526,77 -> 526,80",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "508,27 -> 508,29 -> 503,29 -> 503,35 -> 512,35 -> 512,29 -> 510,29 -> 510,27",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "515,89 -> 520,89",
    "521,152 -> 526,152",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "511,46 -> 515,46",
    "522,80 -> 522,75 -> 522,80 -> 524,80 -> 524,71 -> 524,80 -> 526,80 -> 526,77 -> 526,80",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "507,152 -> 512,152",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "532,87 -> 537,87",
    "531,150 -> 536,150",
    "491,155 -> 491,157 -> 490,157 -> 490,160 -> 501,160 -> 501,157 -> 497,157 -> 497,155",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "522,80 -> 522,75 -> 522,80 -> 524,80 -> 524,71 -> 524,80 -> 526,80 -> 526,77 -> 526,80",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "515,123 -> 531,123 -> 531,122",
    "508,27 -> 508,29 -> 503,29 -> 503,35 -> 512,35 -> 512,29 -> 510,29 -> 510,27",
    "522,80 -> 522,75 -> 522,80 -> 524,80 -> 524,71 -> 524,80 -> 526,80 -> 526,77 -> 526,80",
    "511,42 -> 515,42",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "491,155 -> 491,157 -> 490,157 -> 490,160 -> 501,160 -> 501,157 -> 497,157 -> 497,155",
    "528,85 -> 533,85",
    "505,42 -> 509,42",
    "495,15 -> 495,16 -> 501,16 -> 501,15",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "524,150 -> 529,150",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "499,19 -> 499,21 -> 497,21 -> 497,24 -> 508,24 -> 508,21 -> 505,21 -> 505,19",
    "532,61 -> 536,61",
    "536,89 -> 541,89",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "491,155 -> 491,157 -> 490,157 -> 490,160 -> 501,160 -> 501,157 -> 497,157 -> 497,155",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "499,19 -> 499,21 -> 497,21 -> 497,24 -> 508,24 -> 508,21 -> 505,21 -> 505,19",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "522,80 -> 522,75 -> 522,80 -> 524,80 -> 524,71 -> 524,80 -> 526,80 -> 526,77 -> 526,80",
    "520,148 -> 525,148",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "535,152 -> 540,152",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "527,49 -> 527,51 -> 523,51 -> 523,55 -> 536,55 -> 536,51 -> 531,51 -> 531,49",
    "499,19 -> 499,21 -> 497,21 -> 497,24 -> 508,24 -> 508,21 -> 505,21 -> 505,19",
    "508,27 -> 508,29 -> 503,29 -> 503,35 -> 512,35 -> 512,29 -> 510,29 -> 510,27",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "502,44 -> 506,44",
    "548,104 -> 548,105 -> 559,105 -> 559,104",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "514,44 -> 518,44",
    "517,150 -> 522,150",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "495,15 -> 495,16 -> 501,16 -> 501,15",
    "499,19 -> 499,21 -> 497,21 -> 497,24 -> 508,24 -> 508,21 -> 505,21 -> 505,19",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "535,64 -> 539,64",
    "515,123 -> 531,123 -> 531,122",
    "517,42 -> 521,42",
    "520,44 -> 524,44",
    "510,150 -> 515,150",
    "529,64 -> 533,64",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "499,46 -> 503,46",
    "527,49 -> 527,51 -> 523,51 -> 523,55 -> 536,55 -> 536,51 -> 531,51 -> 531,49",
    "527,49 -> 527,51 -> 523,51 -> 523,55 -> 536,55 -> 536,51 -> 531,51 -> 531,49",
    "510,140 -> 510,141 -> 521,141 -> 521,140",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "522,80 -> 522,75 -> 522,80 -> 524,80 -> 524,71 -> 524,80 -> 526,80 -> 526,77 -> 526,80",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "491,155 -> 491,157 -> 490,157 -> 490,160 -> 501,160 -> 501,157 -> 497,157 -> 497,155",
    "522,89 -> 527,89",
    "505,46 -> 509,46",
    "508,40 -> 512,40",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "523,146 -> 528,146",
    "518,87 -> 523,87",
    "495,15 -> 495,16 -> 501,16 -> 501,15",
    "516,146 -> 521,146",
    "511,38 -> 515,38",
    "491,155 -> 491,157 -> 490,157 -> 490,160 -> 501,160 -> 501,157 -> 497,157 -> 497,155",
    "510,140 -> 510,141 -> 521,141 -> 521,140",
    "499,19 -> 499,21 -> 497,21 -> 497,24 -> 508,24 -> 508,21 -> 505,21 -> 505,19",
    "522,80 -> 522,75 -> 522,80 -> 524,80 -> 524,71 -> 524,80 -> 526,80 -> 526,77 -> 526,80",
    "533,102 -> 533,93 -> 533,102 -> 535,102 -> 535,95 -> 535,102 -> 537,102 -> 537,99 -> 537,102 -> 539,102 -> 539,97 -> 539,102 -> 541,102 -> 541,92 -> 541,102 -> 543,102 -> 543,94 -> 543,102 -> 545,102 -> 545,99 -> 545,102 -> 547,102 -> 547,95 -> 547,102 -> 549,102 -> 549,101 -> 549,102",
    "508,27 -> 508,29 -> 503,29 -> 503,35 -> 512,35 -> 512,29 -> 510,29 -> 510,27",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
    "495,136 -> 495,127 -> 495,136 -> 497,136 -> 497,135 -> 497,136 -> 499,136 -> 499,129 -> 499,136 -> 501,136 -> 501,133 -> 501,136 -> 503,136 -> 503,135 -> 503,136 -> 505,136 -> 505,135 -> 505,136 -> 507,136 -> 507,130 -> 507,136 -> 509,136 -> 509,130 -> 509,136 -> 511,136 -> 511,127 -> 511,136 -> 513,136 -> 513,127 -> 513,136",
    "524,83 -> 529,83",
    "491,155 -> 491,157 -> 490,157 -> 490,160 -> 501,160 -> 501,157 -> 497,157 -> 497,155",
    "519,144 -> 524,144",
    "506,118 -> 506,115 -> 506,118 -> 508,118 -> 508,112 -> 508,118 -> 510,118 -> 510,115 -> 510,118 -> 512,118 -> 512,114 -> 512,118 -> 514,118 -> 514,108 -> 514,118 -> 516,118 -> 516,110 -> 516,118 -> 518,118 -> 518,116 -> 518,118 -> 520,118 -> 520,115 -> 520,118",
]


def run(data, debug=False):
    results = 0
    left = 999999
    right = 0
    depth = 0
    grid = []
    sand_start = (500, 0)

    for row in data:
        points = row.split(" -> ")
        for point in points:
            x, y = point.split(",")
            x = int(x)
            y = int(y)

            left = min(left, x)
            right = max(right, x)
            depth = max(depth, y)

    if debug:
        print(left, right, depth)
    grid = [["."] * (right - left + 1) for i in range(depth + 1)]
    sand_start = (sand_start[0] - left, sand_start[1])
    grid[sand_start[1]][sand_start[0]] = "+"

    if debug:
        show(grid)

    for row in data:
        points = row.split(" -> ")
        for i in range(len(points) - 1):
            x1, y1 = points[i].split(",")
            x2, y2 = points[i + 1].split(",")
            x1 = int(x1) - left
            y1 = int(y1)
            x2 = int(x2) - left
            y2 = int(y2)

            if abs(x1 - x2) == 0:
                # vertical
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[y][x1] = "#"
            else:
                # horizontal
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y1][x] = "#"

    #            if debug: show(grid)

    sand_count = 1
    while drop_sand(sand_start[0], sand_start[1], grid, debug):
        sand_count += 1
    return sand_count - 1

    return results


def drop_sand(x, y, grid, debug):
    try:
        while grid[y + 1][x] == ".":
            y += 1

        # check diagonal left
        if grid[y + 1][x - 1] == ".":
            return drop_sand(x - 1, y, grid, debug)
        # check diagonal right
        elif grid[y + 1][x + 1] == ".":
            return drop_sand(x + 1, y, grid, debug)
        else:
            grid[y][x] = "*"
            if debug:
                show(grid)
            grid[y][x] = "o"
            return True
    except IndexError as e:
        return False


def show(grid):
    print()
    for y in range(len(grid)):
        print("".join([str(x) for x in grid[y]]))


if __name__ == "__main__":
    #    results = run(DATA_TEST, debug=True)
    results = run(DATA, debug=False)
    print("ANSWER:", results)
