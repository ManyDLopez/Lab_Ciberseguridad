#!/usr/bin/env bash
set -euo pipefail

GIT_usr=$1
curl "https://api.github.com/users/$GIT_usr/repos"

