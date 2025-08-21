# Comprehensive Evaluation Summary

**Timestamp:** Thu Aug 21 14:36:33 UTC 2025
**Model:** vllm-model
**Server:** http://localhost:8080

## Test Results

### 1. Feature Tests
- **Status:** ❌ Failed
- **Log:** feature_tests.log

#### Feature Test Summary (last 10 lines):
```
Exception: 1 tests failed out of 4
Configuration: {'server_engine': 'sgLang', 'server_version': 'v0.4.10.post2.6e6f9c7-cu126', 'server_api': 'http://localhost:8080/v1/chat/completions', 'model_name': 'vllm-model'}
Traceback (most recent call last):
  File "/home/vasheno/sanity_check/openai_chat_feature_tests.py", line 341, in <module>
    main()
  File "/home/vasheno/sanity_check/openai_chat_feature_tests.py", line 331, in main
    raise Exception(
Exception: 1 tests failed out of 4
```

### 2. Version Comparison
- **Status:** ✅ Completed
- **Results:** version_comparison.csv
- **Log:** version_comparison.log

#### Version Comparison Details:
```
    Position 5: 4 times (16.7%)
    Position 22: 3 times (12.5%)
    Position 23: 3 times (12.5%)
    Position 37: 3 times (12.5%)
    Position 21: 3 times (12.5%)

  Difference types:
    token_mismatch: 24 (100.0%)

  Difference timing:
    Early differences (pos < 10): 6 (25.0%)
    Late differences (pos >= 10): 18 (75.0%)

============================================================
COMPARISON SUMMARY
============================================================
  Current Version: v0.4.10.post2.6e6f9c7-cu126
  Baseline Version: v0.6.4.post1.0c9082a1
  Total tests: 33
  Mismatches: 24
  Missing baseline: 0
  Detailed analysis saved to: /home/vasheno/sanity_check/evaluation_results_sgLang_v0_4_10_post2_6e6f9c7-cu126_20250821_134102/version_comparison.csv

Done!
```

### 3. Consistency Checks
- **Status:** ✅ Completed
- **Log:** consistency_check.log

#### Consistency Check Summary (last 8 lines):
```
2025-08-21 13:47:23,103 - INFO - ============================================================
2025-08-21 13:47:23,103 - INFO - CONSISTENCY CHECK SUMMARY
2025-08-21 13:47:23,103 - INFO - ============================================================
2025-08-21 13:47:23,103 - INFO - Sequential tests average consistency rate: 100.00%
2025-08-21 13:47:23,103 - INFO - Concurrent tests average consistency rate: 93.45%
2025-08-21 13:47:23,103 - INFO - Overall average consistency rate: 96.73%
2025-08-21 13:47:23,103 - INFO - ============================================================
Configuration: {'server_engine': 'sgLang', 'server_version': 'v0.4.10.post2.6e6f9c7-cu126', 'server_api': 'http://localhost:8080/v1/chat/completions', 'model_name': 'vllm-model'}
```

### 4. lm_eval (MMLU Pro)
- **Status:** ✅ Completed
- **Results:** lm_eval_results/
- **Log:** lm_eval.log

#### lm_eval Results (last 5 lines):
```

| Groups |Version|    Filter    |n-shot|  Metric   |   |Value |   |Stderr|
|--------|------:|--------------|------|-----------|---|-----:|---|-----:|
|mmlu_pro|      2|custom-extract|      |exact_match|↑  |0.7104|±  |0.0041|

```

### 5. BFCL (Function Calling)
- **Status:** ✅ Completed
- **Results:** Check BFCL_PROJECT_ROOT: /home/vasheno/sanity_check/evaluation_results_sgLang_v0_4_10_post2_6e6f9c7-cu126_20250821_134102/bfcl_results
- **Logs:** bfcl.log, bfcl_eval.log

#### BFCL Overall Accuracy:
```
Rank,Overall Acc
1,19.82%
```

### 6. LooGLE (Long Document QA)
- **Status:** ✅ Completed
- **Results:** loogle_results/
- **Log:** loogle.log

#### LooGLE Results (last 2 lines):
```
Scoring batches:   0%|          | 0/18 [00:00<?, ?it/s]Scoring batches:   6%|▌         | 1/18 [00:07<02:15,  7.99s/it]Scoring batches:  11%|█         | 2/18 [00:13<01:45,  6.60s/it]Scoring batches:  17%|█▋        | 3/18 [00:19<01:33,  6.26s/it]Scoring batches:  22%|██▏       | 4/18 [00:25<01:27,  6.26s/it]Scoring batches:  28%|██▊       | 5/18 [00:32<01:21,  6.27s/it]Scoring batches:  33%|███▎      | 6/18 [00:40<01:24,  7.02s/it]Scoring batches:  39%|███▉      | 7/18 [00:48<01:20,  7.31s/it]Scoring batches:  44%|████▍     | 8/18 [00:53<01:05,  6.59s/it]Scoring batches:  50%|█████     | 9/18 [00:56<00:50,  5.56s/it]Scoring batches:  56%|█████▌    | 10/18 [01:00<00:38,  4.85s/it]Scoring batches:  61%|██████    | 11/18 [01:05<00:36,  5.14s/it]Scoring batches:  67%|██████▋   | 12/18 [01:11<00:31,  5.19s/it]Scoring batches:  72%|███████▏  | 13/18 [01:17<00:27,  5.46s/it]Scoring batches:  78%|███████▊  | 14/18 [01:21<00:20,  5.17s/it]Scoring batches:  83%|████████▎ | 15/18 [01:26<00:14,  4.98s/it]Scoring batches:  89%|████████▉ | 16/18 [01:30<00:09,  4.74s/it]Scoring batches:  94%|█████████▍| 17/18 [01:36<00:05,  5.22s/it]Scoring batches: 100%|██████████| 18/18 [01:38<00:00,  4.08s/it]Scoring batches: 100%|██████████| 18/18 [01:38<00:00,  5.45s/it]
Average BERTScore (F1): 84.93%
```

## Files Generated
- evaluation.log
- feature_tests.log
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_010_52053bfb_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_002_a5985e07_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_007_9151a846_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_000_4491cff4_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_003_1b24647b_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_001_72261cc0_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_006_f4dd7e8d_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_005_2ae6d653_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_009_90e12500_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_004_78fe0856_results.json
- vllm-model_sgLang_v0_4_10_post2_6e6f9c7-cu126/prompt_008_82f83a61_results.json
- bfcl_results/score/data_multi_turn.csv
- bfcl_results/score/data_live.csv
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multi_turn_long_context_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_irrelevance_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_simple_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_javascript_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_parallel_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multi_turn_miss_param_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multi_turn_miss_func_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_simple_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_parallel_multiple_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_relevance_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_parallel_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_multiple_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multi_turn_base_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_parallel_multiple_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multiple_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_java_score.json
- bfcl_results/score/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_irrelevance_score.json
- bfcl_results/score/data_non_live.csv
- bfcl_results/score/data_overall.csv
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_irrelevance_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_javascript_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_simple_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multi_turn_long_context_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_java_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multiple_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_relevance_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multi_turn_miss_param_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multi_turn_base_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_parallel_multiple_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_parallel_multiple_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_simple_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_parallel_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_multi_turn_miss_func_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_parallel_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_irrelevance_result.json
- bfcl_results/result/meta-llama_Llama-4-Maverick-17B-128E-Instruct-FP8-FC/BFCL_v3_live_multiple_result.json
- lm_eval_results/vllm-model/results_2025-08-21T14-12-45.178922.json
- version_comparison.log
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_010_52053bfb_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_002_a5985e07_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_007_9151a846_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_000_4491cff4_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_003_1b24647b_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_001_72261cc0_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_006_f4dd7e8d_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_005_2ae6d653_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_009_90e12500_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_004_78fe0856_results.json
- vllm-model_vLLM_v0_6_4_post1_0c9082a1/prompt_008_82f83a61_results.json
- EVALUATION_SUMMARY.md
- consistency_check.log
- loogle.log
- lm_eval.log
- bfcl.log
- bfcl_eval.log
- version_comparison.csv
