
records = [{'CRTE_DTM': '2023-11-29T07:13:24.719+00:00', 'SRC_REGION': 'PA02', 'SRC_CMP': 'VSB', 'SRC_OOID': 'G4ZDWFR3TZ1BPXTW', 'RELATION': 'SPIN', 'DEST_REGION': 'PA02', 'DEST_CMP': 'OTT', 'DEST_OOID': None}, {'CRTE_DTM': '2023-12-04T02:38:27.729+00:00', 'SRC_REGION': 'PA02', 'SRC_CMP': 'CFF', 'SRC_OOID': '1111111111111111', 'RELATION': 'SPIN', 'DEST_REGION': 'PA02', 'DEST_CMP': '008', 'DEST_OOID': 'G39WTZ83SDZPNBMG'}, {'CRTE_DTM': '2023-12-04T04:12:57.847+00:00', 'SRC_REGION': 'PA02', 'SRC_CMP': 'CFF', 'SRC_OOID': '1111111111111111', 'RELATION': 'SPIN', 'DEST_REGION': 'PA02', 'DEST_CMP': 'KLF', 'DEST_OOID': 'G3C94ZNXCX3W716S'}, {'CRTE_DTM': '2023-12-05T14:08:10.602+00:00', 'SRC_REGION': 'PA02', 'SRC_CMP': 'K17', 'SRC_OOID': ' ', 'RELATION': 'RIT', 'DEST_REGION': 'PA02', 'DEST_CMP': '81K', 'DEST_OOID': '5578BC84D0D00010'}, {'CRTE_DTM': '2023-12-05T14:31:02.488+00:00', 'SRC_REGION': 'PA02', 'SRC_CMP': 'K17', 'SRC_OOID': ' ', 'RELATION': 'RIT', 'DEST_REGION': 'PA02', 'DEST_CMP': '81K', 'DEST_OOID': '5578BC84D0D00010'}]

#option 1
R = Row('response_json')
response_df = spark.createDataFrame([R(x) for i,x in enumerate(records)])
response_json_df = response_df.withColumn("_c", F.to_json("response_json"))
company_transfer_df = response_json_df.withColumn("_c", F.from_json("_c", company_transfer_schema)) \
                                    .select("_c.*","response_json") \
                                    .withColumn('REQUESTED_RG',lit(region_code))
company_transfer_df.write.mode("append").saveAsTable(name=f"ssot_blue_turbo_fit.ap_company_transfers",partitionBy=['REQUESTED_RG'])

