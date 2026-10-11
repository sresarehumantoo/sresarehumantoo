<div align="center">
  <img src="banner.jpg" alt="Isometric CI/CD conveyor where one scanning arch turns red over a flagged artifact" width="100%">
  <h1>Owen Pierce</h1>
  <p><b>Security Engineer: cloud, DevSecOps, and offensive security.</b></p>

  <a href="https://www.linkedin.com/in/prodguardian/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <img src="https://img.shields.io/badge/HTB-CPTS%20%C2%B7%20CDSA-9FEF00?style=for-the-badge&logo=hackthebox&logoColor=black" alt="HTB CPTS and CDSA">
</div>

<div align="center">
  <img src="terminal.svg" width="760" alt="Terminal session. $ whoami -> owen, security engineer at Ally. $ cat ~/.history -> sre: ran production AWS with Terraform and CI/CD; soc: worked the queue as the team's AWS SME; sec eng: cloud and pipeline security, internal offensive testing. $ ls ~/focus -> ai-security, cloud-security, devsecops, infrastructure-as-code, pipeline-security, offsec.">
</div>

I sit on a team with threat hunting, detection engineering, and automation engineering. My lane is cloud and DevSecOps security: hardening AWS and CI/CD, writing the occasional detection, and assessing our own platforms the way an attacker would.

### Things I've built

| Project | What it does |
|:--|:--|
| **[reaper](https://github.com/sresarehumantoo/reaper)** <br> ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white) | JavaScript/TypeScript malware deobfuscation and triage. Static dead-code and obfuscation analysis plus a hardened Docker sandbox for dynamic runs. |
| **[wsmancer](https://github.com/sresarehumantoo/wsmancer)** <br> ![Go](https://img.shields.io/badge/-Go-00ADD8?logo=go&logoColor=white) | PSRP-native WinRM shell for offensive Windows work. NTLM/Kerberos message sealing, typed JSON output, sessions that survive dropped connections. |
| **[rummage](https://github.com/rummage-dev/rummage)** <br> ![Go](https://img.shields.io/badge/-Go-00ADD8?logo=go&logoColor=white) | TUI file picker and fuzzy finder library for Go, built on Bubble Tea. |
| **[dotfiles](https://github.com/sresarehumantoo/dotfiles)** <br> ![Go](https://img.shields.io/badge/-Go-00ADD8?logo=go&logoColor=white) | Idempotent, reversible workstation configurator for Linux and macOS, with dry-run and drift detection. |
| **[htb-hosts](https://github.com/sresarehumantoo/htb-hosts)** <br> ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | Sudo-free `/etc/hosts` manager for Hack The Box, as a CLI and a zero-dependency MCP server. |

**Upstream:** [neovim/neovim: treesitter foldexpr parsing mid-change](https://github.com/neovim/neovim/pulls?q=author%3Asresarehumantoo)

### Behind the curtain

Most of my infrastructure work lives in a private GitLab: about 100 Ansible roles and Terraform across 25+ repos running a segmented homelab.

<p>
  <img src="https://img.shields.io/badge/Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white" alt="Terraform">
  <img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible">
  <img src="https://img.shields.io/badge/Vault-FFEC6E?style=flat-square&logo=vault&logoColor=black" alt="Vault">
  <img src="https://img.shields.io/badge/Teleport-512FC9?style=flat-square&logo=teleport&logoColor=white" alt="Teleport">
  <img src="https://img.shields.io/badge/Headscale-242424?style=flat-square&logo=tailscale&logoColor=white" alt="Headscale">
  <img src="https://img.shields.io/badge/Suricata_IPS-EF7B4D?style=flat-square" alt="Suricata">
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white" alt="Proxmox">
  <img src="https://img.shields.io/badge/VyOS-1B2A3A?style=flat-square" alt="VyOS">
</p>

- Zero standing privilege: Vault with default-deny, short-lived scoped tokens so automation and AI agents never hold admin credentials
- 15 segmented VLANs behind Suricata inline IPS; Headscale, Teleport (WebAuthn), and Authelia SSO for access
- An Active Directory attack range built from a Packer golden image, with Terraform and Ansible injecting repeatable misconfigurations
- Routers, DNS/DHCP, hypervisors, and services converge from Ansible and Terraform in CI

### Certifications

HTB CPTS · HTB CDSA · AWS Solutions Architect Associate · HashiCorp Terraform Associate · CompTIA CySA+ · CompTIA Security+
