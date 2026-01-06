import py3_logger

import py3_execute


def test_execute():
    # language=javascript
    js_code = '''
              function sdk () {
                let sum = 0;
                for (const n of arguments) {
                  if (typeof n === "number") sum += n;
                }
                return sum;
              } \
              '''
    result = py3_execute.js.execute_javascript_by_execjs(js_code, func_name="sdk", func_args=(1, 2, "3"))
    print(result)

    # language=javascript
    js_code = '''
              function sdk () {
                let sum = 0;
                for (const n of arguments) {
                  if (typeof n === "number") sum += n;
                }
                return sum;
              } \
              '''
    result = py3_execute.js.execute_javascript_by_py_mini_racer(js_code, func_name="sdk", func_args=(1, 2, "3"))
    print(result)

    # language=javascript
    js_code = '''(function () {
      arguments = process.argv.slice(1).map(JSON.parse);
      let sum = 0;
      for (const n of arguments) {
        if (typeof n === "number") sum += n;
      }
      console.log(JSON.stringify({ "sum": sum }));
    })();'''

    result = py3_execute.js.execute_javascript_by_subprocess(js_code, arguments=(1, 2, "3",))
    print(result["sum"])

    logger = py3_logger.get_logger(__name__)
    py3_execute.cmd.execute_cmd_code_by_subprocess_popen("ping www.baidu.com", "cp936", logger)
    py3_execute.cmd.execute_cmd_code_by_subprocess_run("ping www.baidu.com", "cp936", logger)
    print(py3_execute.cmd.execute_cmd_code_by_subprocess_popen("pip show py3-execute", "cp936", logger))
    print(py3_execute.cmd.execute_cmd_code_by_subprocess_popen("pip show orjson", "cp936", logger))


if __name__ == '__main__':
    test_execute()
