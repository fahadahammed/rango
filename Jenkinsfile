pipeline {
  agent any
  stages {
    stage('build') {
      steps {
	sh 'echo ${USER};pwd'
        sh 'echo Building ${BRANCH_NAME}...'
      }
    }
  }
}
