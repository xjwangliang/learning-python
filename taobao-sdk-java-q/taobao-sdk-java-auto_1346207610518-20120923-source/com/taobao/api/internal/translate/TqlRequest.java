package com.taobao.api.internal.translate;

import java.util.Map;

import com.taobao.api.ApiRuleException;
import com.taobao.api.TaobaoRequest;
import com.taobao.api.TaobaoResponse;
import com.taobao.api.internal.util.RequestCheckUtils;
import com.taobao.api.internal.util.TaobaoHashMap;

public class TqlRequest<T extends TaobaoResponse> implements TaobaoRequest<T> {

	public static final String TOP_TQL_SEPERATOR = "top_tql_seperator";
	private TaobaoHashMap udfParams;
	private Long timestamp;
	private String ql;
	private Class<T> rspClass;

	public TqlRequest(Class<T> rspClass) {
		this.rspClass = rspClass;
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
		txtParams.put("ql", this.ql);
		txtParams.put(TOP_TQL_SEPERATOR, true);
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

	public Class<T> getResponseClass() {
		return rspClass;
	}

	public void check() throws ApiRuleException {
		RequestCheckUtils.checkNotEmpty(ql, "ql");
	}
}
