import random
import time
import requests

# import gpt_2_simple as gpt2
import multiprocessing as mp


class GPT2:

    def start_threaded(self, file_name, model_name, conn, queue):
        return mp.Process(target=self.handler_process, args=(file_name, model_name, conn, queue))

    def handler_process(self, file_name, model_name, conn, queue):
        # sess = self.finetune(file_name=file_name, model_name=model_name)
        # conn.send("Finished")
        # res = queue.get()
        # res['sess'] = sess
        # queue.put(res)
        l = []
        for i in range(20):
            time.sleep(1)
            l.append(random.randint(1, 100))
        conn.send("Finished")
        # res = queue.get()

        queue.put([l])
        print("hp finished")
        requests.post("http://localhost:5000/ping", data={"finished": True})
    #
    # def finetune(self, file_name, model_name):
    #     sess = gpt2.start_tf_sess()
    #     print("GPT-2 beginning fine-tuning using " + file_name + " as the corpus")
    #     gpt2.finetune(sess,
    #                   file_name,
    #                   model_name=model_name,
    #                   steps=1000)  # steps is max number of training steps
    #     return sess
    #
    # def generate_text(self, sess):
    #     single_text = gpt2.generate(sess, return_as_list=True)[0]
    #     return single_text
