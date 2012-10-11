package com.taobao.api.internal.translate;

import java.util.Date;
import java.util.Map;

import com.taobao.api.ApiRuleException;
import com.taobao.api.TaobaoRequest;
import com.taobao.api.TaobaoResponse;
import com.taobao.api.internal.util.RequestCheckUtils;
import com.taobao.api.internal.util.TaobaoHashMap;

public class ScheduleApiRequest implements TaobaoRequest<TopatsScheduleAddResponse> {
	
	public static final String TOP_TQL_SEPERATOR = "top_tql_seperator";
	private TaobaoHashMap udfParams;
	private Long timestamp;
	private String ql;
	private Date schedule;
	private TaobaoRequest<? extends TaobaoResponse> taobaoRequest;
	
	public void setSchedule(Date schedule) {
		this.schedule = schedule;
	}

	public void setTaobaoRequest(TaobaoRequest<? extends TaobaoResponse> taobaoRequest) throws ApiRuleException {
		this.taobaoRequest = taobaoRequest;
		taobaoRequest.check();
	}

	public String getQl() {
		return ql;
	}

	public void setQl(String ql) {
		this.ql = ql;
	}
	
	public Long getTimestamp() {
		return this.timestamp;
	}

	public void setTimestamp(Long timestamp) {
		this.timestamp = timestamp;
	}

	public String getApiMethodName() {
		return null;
	}

	public Map<String, String> getTextParams() {
		TaobaoHashMap txtParams = new TaobaoHashMap();
		txtParams.put("isTql", false);
		txtParams.put("schedule", schedule);
		if (taobaoRequest != null) {
			if (taobaoRequest instanceof TqlRequest) {
				txtParams.put("isTql", true);
				txtParams.put(TOP_TQL_SEPERATOR, true);
			} else {
				txtParams.put("method", taobaoRequest.getApiMethodName());
			}
			txtParams.putAll(taobaoRequest.getTextParams());
		} else if (null != this.ql) {
			txtParams.put("ql", this.ql);
			txtParams.put(TOP_TQL_SEPERATOR, true);
			txtParams.put("isTql", true);
		}
		if (this.udfParams != null) {
			txtParams.putAll(this.udfParams);
		}
		return txtParams;
	}

	public void putOtherTextParam(String key, String value) {
		if (this.udfParams == null) {
			this.udfParams = new TaobaoHashMap();
		}
		this.udfParams.put(key, value);
	}

	public Class<TopatsScheduleAddResponse> getResponseClass() {
		return TopatsScheduleAddResponse.class;
	}

	public void check() throws ApiRuleException {
		RequestCheckUtils.checkNotEmpty(schedule,"schedule");
	}
}
