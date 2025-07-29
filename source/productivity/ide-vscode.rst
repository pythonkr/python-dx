.. _ide_vscode:

VSCode
==========

VSCode 에서는 다음의 확장은 기본적으로 설치를 권장합니다.

* Python
* Pylance
* ruff
* pyright ( 타입을 필요로 하는 경우 )

Pylance
-------

VSCode의 Python Extension은 Pylance라는 Language Server를 사용합니다.
Pylance는 자동완성, 코드 분석 등 다양한 기능을 제공하지만,
기본 설정으로는 자동완성 기능이 많이 부족합니다.

Pylance의 분석 범위를 프로젝트 전체로 확장하려면 ``python.analysis.languageServerMode`` 값을 ``full`` 로 설정합니다. 이렇게 하면 모든 파일에 대한 전체 분석을 활성화하여, 정확도를 높일 수 있습니다.

.. code-block:: json

   // .vscode/settings.json
   {
     "python.analysis.languageServerMode": "full"
   }

Ruff
----

`Ruff <https://docs.astral.sh/ruff/>`_ 는 매우 빠른 Python Linter 및 Formatter입니다. Ruff를 사용하면 ``flake8``, ``isort``, ``black`` 등 다양한 도구를 대체할 수 있습니다.

VSCode에 `Ruff Extension <https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff>`_ 을 설치하면 저장 시 자동으로 코드 검사 및 포맷팅을 수행하도록 설정할 수 있습니다.

.. code-block:: json

   // .vscode/settings.json
   {
     "[python]": {
       "editor.defaultFormatter": "charliermarsh.ruff",
       "editor.formatOnSave": true,
       "editor.codeActionsOnSave": {
         "source.fixAll": "explicit",
         "source.organizeImports": "explicit"
       }
     }
   }

Pyright
-------

`Pyright <pyright.html>`_ 는 Pylance의 기반이 되는 강력한 정적 타입 검사기입니다. Pylance가 제공하는 기능 외에 추가적인 고급 설정이나 CLI 환경에서의 빠른 타입 검사를 원할 때 직접 사용할 수 있습니다.

VSCode에서 Pylance 대신 Pyright를 직접 사용하려면, 먼저 Python 확장 프로그램의 Language Server 설정을 "Default"에서 "Pylance"가 아닌 다른 것으로 변경하거나, Pylance 확장 프로그램을 비활성화해야 합니다. 그 후, `Pyright VSCode 확장 프로그램 <https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright>`_ 을 설치합니다.

일반적으로는 Pylance를 사용하는 것이 가장 편리하지만, 특정 프로젝트에서 Pyright의 세밀한 제어가 필요하거나, Pylance의 동작 방식에 문제가 있을 때 대안으로 고려할 수 있습니다.