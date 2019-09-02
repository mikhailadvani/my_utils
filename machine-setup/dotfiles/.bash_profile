export GIT_AUTHOR_NAME=$(git config user.name)
export GIT_AUTHOR_EMAIL=$(git config user.email)
export GIT_COMMITTER_NAME=$(git config user.name)
export GIT_COMMITTER_EMAIL=$(git config user.email)
alias ll="ls -l"
alias l1="ls -1"
alias git_pr="git pr && git submodule update --recursive --remote"
alias git_prune="git co master && git pr && git branch --merged | grep -v 'master' | xargs -n 1 git branch -D"
alias venv_setup_2="/usr/local/bin/virtualenv -p $(which python2) .venv"
alias venv_setup_3="/usr/local/bin/virtualenv -p $(which python3) .venv"

alias init_terra="/usr/local/bin/terraform init -backend-config=backend.tfvars"
alias plan_terra="/usr/local/bin/terraform plan"
alias apply_terra="/usr/local/bin/terraform apply"
alias outputs_terra="/usr/local/bin/terraform output"
alias refresh_terra="/usr/local/bin/terraform refresh"
alias clean_terra="find . -name .terraform -type d | xargs rm -r"

# 2 line kube-ps1 context
if [ -f $HOME/work/mikhailadvani/kube-ps1/kube-ps1.sh ]; then
  source "$HOME/work/mikhailadvani/kube-ps1/kube-ps1.sh"
  PS1='$(kube_ps1)'$PS1
fi

# The next line is to allow cross account authentication in terraform
export AWS_SDK_LOAD_CONFIG=1
export GOPATH=$HOME/go
