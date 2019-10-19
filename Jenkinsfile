pipeline {
  agent any
  stages {
    stage('build') {
      steps {
	sh 'echo ${USER};pwd;echo ${HOME}'
        sh 'echo Building ${BRANCH_NAME}...'
      }
    }
  }
}
