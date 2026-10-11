### Owen Pierce

Security engineer at Ally, on a team covering threat hunting, detection engineering, and automation. I came up through SRE and the SOC, so most of what I build is tooling meant to be operated: malware triage, Windows protocol work, least-privilege access for automation and AI agents, and a homelab run entirely as code.

**Things I've built**

| | |
|---|---|
| [reaper](https://github.com/sresarehumantoo/reaper) | JavaScript/TypeScript malware deobfuscation and triage, with a hardened Docker sandbox for dynamic analysis |
| [wsmancer](https://github.com/sresarehumantoo/wsmancer) | PSRP-native WinRM client in Go with NTLM/Kerberos message sealing |
| [rummage](https://github.com/rummage-dev/rummage) | TUI file picker and fuzzy finder library for Go, built on Bubble Tea |
| [dotfiles](https://github.com/sresarehumantoo/dotfiles) | Idempotent, reversible workstation configurator in Go with dry-run and drift detection |
| [htb-hosts](https://github.com/sresarehumantoo/htb-hosts) | Sudo-free `/etc/hosts` manager for Hack The Box, as a CLI and an MCP server |

Most of my infrastructure work lives in a private GitLab: about 100 Ansible roles and Terraform across 25+ repos running a segmented homelab with a Headscale overlay, Teleport, HashiCorp Vault, and Suricata inline IPS.

HTB CPTS and CDSA · AWS Solutions Architect Associate · Terraform Associate

[aboutowenpierce.com](https://aboutowenpierce.com) · [LinkedIn](https://www.linkedin.com/in/prodguardian/)
