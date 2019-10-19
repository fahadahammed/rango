pipeline {
  agent any
  stages {
    stage('build') {
      steps {
	sh '/usr/bin/kubectl get pods'
        sh 'echo Building ${BRANCH_NAME}...'
      }
    }
  }
}
