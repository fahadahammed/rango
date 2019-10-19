pipeline {
  agent any
  stages {
    stage('build') {
	when { expression { BRANCH_NAME == "master"} }  
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

	when { expression { BRANCH_NAME == "stage"} }

		steps {
                sh 'echo ${USER};pwd;echo ${HOME}'
                sh 'echo Building ${BRANCH_NAME}...'
                sh '/usr/bin/kubectl get pods'
		sh "sed -i 's|VVVV|s${currentBuild.number}|g' app.py"
                sh '/usr/bin/docker build -t rango:s${currentBuild.number} .'
                sh '/usr/bin/docker tag rango:s${currentBuild.number} 172.31.40.211:5000/rango:s${currentBuild.number}'
                sh '/usr/bin/docker push 172.31.40.211:5000/rango:s${currentBuild.number}'
		sh 'cp rango-deployment.yaml /tmp/rd-s${currentBuild.number}.yaml'
		sh "sed -i 's|latest|s${currentBuild.number}|g' /tmp/rd-s${currentBuild.number}.yaml"
		sh '/usr/bin/kubectl create -f /tmp/rd-s${currentBuild.number}.yaml'
		}
        }

       }
    }
  }
}
