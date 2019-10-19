pipeline {
  agent any
  stages {
    stage('build') {
		steps {
		sh 'echo ${USER};pwd;echo ${HOME}'
        	sh 'echo Building ${BRANCH_NAME}...'
		sh '/usr/bin/kubectl get pods'
		sh "sed -i 's|VVVV|s${currentBuild.number}|g' app.py"
		sh '/usr/bin/docker build -t rango:latest .'
		sh '/usr/bin/docker tag rango 172.31.40.211:5000/rango'
		sh '/usr/bin/docker push 172.31.40.211:5000/rango'
		sh '/usr/bin/kubectl set image deployment/rango-app rango=172.31.40.211:5000/rango'
		}

    }
  }
}
