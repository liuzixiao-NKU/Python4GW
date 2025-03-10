# GW_project
My research dashboard

pip install --upgrade pip

pip install -U --pre mxnet-cu91
(optional)
sudo ldconfig /usr/local/cuda-9.1/lib64

pip install line-profiler


openssl md5 -sha256 lscsoft-archive-keyring_2016.06.20-2_all.deb
SHA256(lscsoft-archive-keyring_2016.06.20-2_all.deb)= 6bc13fa2d1f1e10faadea4ba18380a002be869a78988bbc22194202c9ba71697

MY GPU server: 59.64.32.108

--follow

floyd run --gpu  \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "my_comment" \
"bash setup_floydhub.sh && python run.py"

floyd run --gpu --follow \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/15:pretrained \
-m "OURs_7" \
"bash setup_floydhub.sh && python run.py"

floyd run --gpu --follow \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/20:pretrained \
-m "OURs_4" \
"bash setup_floydhub.sh && python run.py"


floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/datasets/checkpoints_cnn_models/15:pretrained \
-m "PRL_21" \
"bash setup_floydhub.sh && python run_PRL.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/datasets/checkpoints_cnn_models/13:pretrained \
-m "PRL_21" \
"bash setup_floydhub.sh && python run.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/datasets/checkpoints_cnn_models/11:pretrained \
-m "PLB_1" \
"bash setup_floydhub.sh && python run_PLB.py"

---

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/datasets/checkpoints_cnn_models/13:pretrained \
-m "AUC_OURs" \
"bash setup_floydhub.sh && python run_eval.py"


floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/datasets/checkpoints_cnn_models/11:pretrained \
-m "AUC_PLB" \
"bash setup_floydhub.sh && python run_eval_PLB.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/datasets/checkpoints_cnn_models/15:pretrained \
-m "AUC_PRL" \
"bash setup_floydhub.sh && python run_eval_PRL.py"


---


floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/45:pretrained \
-m "AUC_PRL21" \
"bash setup_floydhub.sh && python run_eval_PRL.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/46:pretrained \
-m "AUC_OURs" \
"bash setup_floydhub.sh && python run_eval.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/datasets/checkpoints_cnn_models/11:pretrained \
-m "AUC_PLB_1" \
"bash setup_floydhub.sh && python run_eval_PLB.py"


---


floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "OURs_ft_hidden_dim" \
"bash setup_floydhub.sh && python run_ft_hidden_dim.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "OURs_ft_fc_params" \
"bash setup_floydhub.sh && python run_ft_fc_params.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "OURs_ft_dropout" \
"bash setup_floydhub.sh && python run_ft_dropout.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "OURs_ft_act_type" \
"bash setup_floydhub.sh && python run_ft_act_type.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "OURs_ft_dialute" \
"bash setup_floydhub.sh && python run_ft_dialute.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "OURs_ft_num_fiter" \
"bash setup_floydhub.sh && python run_ft_num_filter.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "OURs_ft_pool_params" \
"bash setup_floydhub.sh && python run_ft_pool_params.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "OURs_ft_conv_params" \
"bash setup_floydhub.sh && python run_ft_conv_params.py"



---


floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/68:pretrained \
-m "AUC_OURs_ft_dropout" \
"bash setup_floydhub.sh && python run_eval_ft_dropout.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/70:pretrained \
-m "AUC_OURs_ft_dialute" \
"bash setup_floydhub.sh && python run_eval_ft_dialute.py"


floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/71:pretrained \
-m "AUC_OURs_ft_num_filter" \
"bash setup_floydhub.sh && python run_eval_ft_num_filter.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/69:pretrained \
-m "AUC_OURs_ft_act_type" \
"bash setup_floydhub.sh && python run_eval_ft_act_type.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/66:pretrained \
-m "AUC_OURs_ft_hidden_dim" \
"bash setup_floydhub.sh && python run_eval_ft_hidden_dim.py"


floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/72:pretrained \
-m "AUC_OURs_ft_pool_param" \
"bash setup_floydhub.sh && python run_eval_ft_pool_param.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/67:pretrained \
-m "AUC_OURs_ft_hidden_num" \
"bash setup_floydhub.sh && python run_eval_ft_hidden_num.py"


floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/73:pretrained \
-m "AUC_OURs_ft_convlayer" \
"bash setup_floydhub.sh && python run_eval_ft_convlayer.py"


---


floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
-m "OURs_modified" \
"bash setup_floydhub.sh && python run_modified.py"

floyd run --gpu \
--data wctttty/datasets/gw_waveform/1:waveform \
--data wctttty/projects/python4gw/83:pretrained \
-m "AUC_OURs_ft_dialute" \
"bash setup_floydhub.sh && python run_eval_ft_dialute.py"